from datetime import datetime
from threading import Thread
#from utils import sensecam_analyze_sensor

def sensecam_get_date(time_string):
    '''This function returns minute of events 
    
    :param dt: datetime object 
    :type dt: datetime 
    :returns: normal distribution 
    '''
    #time_format = '%Y/%m/%d %H:%M:%S'
    time_format = '%m/%d/%Y %H:%M:%S %p' # sensecam raw and uploaded
    dt = datetime.strptime(time_string, time_format)
    date = dt.date()
    return date

def test():
    """ This function processes all unuploaded sensecam files directly from sensecam devices, these sensecam files are not previously uploaded using sensecam software.

    :param  capture_time: capture time of this file, only available for image files 
    :type   capture_time: datetime.datetime 

    :return: None
    """
    #filepath = "/home/media/sensecambrowser/sensor/user_1/sensor_2014-05-17_1.csv"
    filepath = "/home/marissa/Desktop/sensor_2014-06-02.csv"
    #images = Image.objects.filter(resized=False).values(file)
    #thread = Thread(target = resize_image_folder, args = (images))
    #thread.start()
    #(albums,file_capture_date) = sensecam_analyze_sensor(filepath,1)
    #print albums.keys()
    #test_filereader(filepath)

    time_str_1 ="5/19/2012 4:14:00 PM"
    date = sensecam_get_date(time_str_1)
    print date

    # does not need to wait until the thread terminates.
    # thread.join()

def main():
    thread = Thread(target = test, args = ())
    thread.start()

#    test()# my code here

if __name__ == "__main__":
    main()

