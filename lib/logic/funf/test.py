from Accelerometer import Accelerometer

path = "/media/ExpData/funf/2014-03-26/test/AccelerometerSensorProbe.csv"
acc = Accelerometer(path)
acc.csv_read()
acc.plotting()
