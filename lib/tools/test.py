from datetime import datetime
from threading import Thread
from utils import AnnotationImporter
from utils import SensorImporter

def test():
    #filepath = "/home/media/sensecambrowser/sensor/user_1/sensor_2014-05-17_1.csv"
    anno_filepath = "/home/marissa/Documents/temp/DIAL212_IO_Annotations.csv"
    sensor_filepath = "/home/marissa/Documents/temp/DIAL212_IO_Annotations.csv"
    #annotationImporter = AnnotationImporter(anno_filepath)
    #annotationImporter.start_import()
    sensorImporter = SensorImporter(sensor_filepath)
    sensorImporter.start_import()
    #images = Image.objects.filter(resized=False).values(file)
    #thread = Thread(target = resize_image_folder, args = (images))
    #thread.start()
    #(albums,file_capture_date) = sensecam_analyze_sensor(filepath,1)
    #print albums.keys()
    #test_filereader(filepath)

    # does not need to wait until the thread terminates.
    # thread.join()

def main():
    thread = Thread(target = test, args = ())
    thread.start()

#    test()# my code here

if __name__ == "__main__":
    main()

