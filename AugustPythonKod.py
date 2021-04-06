from pupil_apriltags import Detector
import cv2
import numpy as np
from time import sleep
import yaml

def length(length):
    """ Calculates the amount of frames between two corners in x-axle, if the apriltag is bend it takes the corners between x, y which has most frames"""
    length_x = length[:, 0]
    length_y = length[:, 1]
    lengths = [length_x, length_y]
    size = []
    for length in lengths:
        length = np.sort(length)[::-1]      # Sorts them with largest first
        length = length[0] - length[2]      # Takes the first and the third because they are beside each other in x-led
        size.append(length)
    if size[0] >= size[1]:
        return size[0]
    return size[1]


def func_2(x):                      # funktion för avståndsmätning
    #return 7.97983012 * np.exp(-0.01026438*x)+0.70805441
    return 9.472138612 * np.exp(-0.01217216*x)+0.7222774 # nya värden, är avståndsmätningen bättre med denna??


def func_2_to_middle_line(x):       # funktion för vinkelmätning
    return 494.37127535 * np.exp(-1.22146463*x)+48.78180416

at_detector = Detector(
	families='tag36h11',
	nthreads=1,
	quad_decimate=1.0,
	quad_sigma=0.0,
	refine_edges=1,
	decode_sharpening=0.25,
	debug=0)


""" Fix so the frames on the camera is constant"""
video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 1920) 
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while(True):
    # Capture frame-by-frame
    ret, frame = video.read()

    # Change the frame to gray scale
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # See what the height and width of the frame is
    height_of_image, width_of_image = img.shape  # width x and height y

    text = [1321, 0, 960, 0, 743, 540, 0, 0, 1]     # camera parameters
    cameraMatrix = np.array(text).reshape((3, 3))
    
    camera_params = (
        cameraMatrix[0, 0], # f_x: focal length = brännvidd (ofta som "synvinkel" = 72 grader), här anges det i pixlar
        cameraMatrix[1, 1], # f_y: focal length = A (=half image size) / tan(synvinkel/2)
        cameraMatrix[0, 2], # c_x: focal center in pixels, center of image
        cameraMatrix[1, 2], # c_y: focal center
    )

    # Detect the apriltags
    frame = at_detector.detect(img, True, camera_params, 0.26)
    color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    for tag in frame:
        #print('corners:',tag.corners)      # användes för att mäta på olika avstånd för att få fram funktionerna
        #print('center:',tag.center)

        """ Draw green box around found tags"""
        for idx in range(len(tag.corners)):
            cv2.line(color_img, tuple(tag.corners[idx - 1, :].astype(int)), tuple(tag.corners[idx, :].astype(int)),(0, 255, 0),)

        """ Write tag ID next to found tags"""
        cv2.putText(
            color_img,
            str(tag.tag_id),
            org=(tag.corners[0, 0].astype(int) + 10, tag.corners[0, 1].astype(int) + 10, ),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=0.8,
            color=(0, 0, 255),
        )

        """ Takes the corners and calculates the distance in frames between 2 of them """
        corners = tag.corners
        length_corners = length(corners)
        length_from_camera = func_2(length_corners)                     # avståndet som skickas till arduinon
        print(length_from_camera)   

        """ Distance from middle line """
        # Middle line is at frame 1920/2 because it is predetermined earlier in the code
        check_16 = 16                                                   # avståndet som vi förflyttat bilden åt vänster vid uppmätning vid olika avstånd
        frame_for_16cm = func_2_to_middle_line(length_from_camera)      # funktion som räknar avstånd till mitten
        center_x = tag.center[0]
        spot = ((center_x-960)/frame_for_16cm)*check_16/100             # meter from middle

        """ Angle to to middle """
        sin = np.sin(spot/length_from_camera)                           # räknar ut vinkeln
        print(np.degrees(sin))


    # Display the resulting frame
    cv2.imshow("Detected tags", color_img)

    """ Waiting x seconds for the iteration, so the odometry will work """
    #sleep(1)    # wait for the iteration

    # kalla på 

    #   Waits for a user input to quit the application, Usable when trying on a computer
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
