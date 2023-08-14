""" Photonics Application Suite (PAS) Interface """
import win32com.client

import time
import numpy as np
import pandas as pd
from typing import Tuple

class BasePAS(object):
    """
    A base Photonics Application Suite class.
    
    This base object is put in here to ensure that people can use other instruments
    even though they are not using Windows OS

    Parameters
    ----------
    server_addr: str
        The address of the software
    """
    def __init__(self, server_addr: str):
        self.engine_mgr = win32com.client.Dispatch(server_addr)
        self.engine = self.engine_mgr.NewEngine()
        self.activate()
        activating = 0
        start = time.time()

        # Check engine activation status
        while activating == 0:
            time.sleep(0.5) 
            activating = self.engine_state()
            if time.time() - start > 30:
                raise TimeoutError("Timeout error: check devices connection")

    def activate(self):
        """ Active the engine. """
        self.engine.Activate()

    def deactivate(self):
        """ Active the deactivate. """
        self.engine.DeActivate()

    def engine_state(self):
        """ Check the engine state. """
        return self.engine.Active
    
    def quit(self):
        """ Quit the engine. """
        self.deactivate()
        self.engine_mgr.DeleteEngine(self.engine)

    def validate_settings(self):
        """ Validate the settings. """
        self.engine.ValidateSettings()

    def __get_name(self) -> str:
        return self.__class__.__name__
    
    def __str__(self) -> str:
        return f"Photonics Application Suite: {self.__get_name()} "
    
    def __repr__(self) -> str:
        return f"{self.__get_name()}()"


class KeysightILME(BasePAS):
    """
    Keysight Insertion Loss Measurement Engine Win32com Library.

    This can control Agilent 8163B.
    """

    def __init__(self):
        self.no_channels = 1
        server_addr = "AgServerIL.EngineMgr"
        super().__init__(server_addr=server_addr)


    def sweep_params(self, start: float=1540, stop: float=1575, step: float=5, power: float=10):
        """ Set sweep parameters. """
        self.engine.WavelengthStart = start * 1e-09
        self.engine.WavelengthStop = stop * 1e-09
        self.engine.WavelengthStep = step * 1e-12 # 0.3 x sweep rate [nm/s] = step size [pm]
        self.engine.TLSPower = pow(10, (power/10)) * 1e-03

    def set_num_of_scans(self, num: int):
        """ Set number of scans. """
        self.engine.NumberOfScans = num

    def start_meas(self):
        """ Start one-shot measurement. """
        self.engine.StartMeasurement()

    def stop_meas(self):
        """ Stop a measurement. """
        self.engine.StopMeasurement()

    def get_no_channels(self) -> int:
        """ Get the number of channels active. """
        return self.no_channels  

    def get_result(self, col_name: int) -> Tuple[tuple, tuple]:
        """ 
        Obtain result after the measurement.
        
        Parameter
        ---------
        col_name: str
            Column name 
        """
        data = pd.DataFrame()

        busy = True

        # Wait for the sweep to finish
        while busy == True:
            time.sleep(0.1)
            busy = self.engine.Busy
        
        IOMRFile = self.engine.MeasurementResult
        IOMRGraph = IOMRFile.Graph("RXTXAvgIL")
        data_per_curve = IOMRGraph.dataPerCurve
        no_channels = IOMRGraph.noChannels
        self.no_channels = no_channels
        ydata = IOMRGraph.YData
        ycurve = [tuple(ydata[i*data_per_curve:(i+1)*data_per_curve]) for i in range(no_channels)]
        for i in range(no_channels):
            data[f"{col_name} - CH{i}"] = ycurve[i]
        
        return self.get_wavelength(IOMRGraph, data_per_curve), data
    
    @staticmethod
    def get_wavelength(IOMRGraph, data_per_curve) -> tuple:
        """ Get all wavelength datapoints from a measurement. """
        xstart = IOMRGraph.xStart
        xstep = IOMRGraph.xStep
        xdata = [xstart + i * xstep for i in range(data_per_curve)]
        return tuple(np.divide(xdata, 1e-9))
    
    @staticmethod
    def export_file(results, fname):
        results.Write(fname)