import predict_model
from shutil import move
from threading import Thread

cry_count = 1
silent_count = 1
flag = 0
cry_count = 0
silent_count = 0


def Baby_Cry_Detction():
    global cry_count, silent_count, flag

    while True:
        print("Recording Audio ... ")
        # call the cry detection model...
        label, file = predict_model.predict()
        
        # if model detects crying...
        if label == 1:
            print("Baby is Crying")
            # crying flag
            flag = 1
            # store 5 seconds cry sample
            move("New.wav", "Crying_baby/raw/"+"Baby_Cry" + str(cry_count) + ".wav")
            # number of 5 seconds cry samples counter
            cry_count += 1

            #TODO create I/O flags 
        
        # if everything is good, baby cry not detected...
        else:
            print("Baby is Silent")
            # Later, you can decide to disable line below in order to save storage...
            move("New.wav", "Silence/"+"Silent_" + str(silent_count) + ".wav")
            silent_count += 1

if __name__ == '__main__':
    Thread(target=Baby_Cry_Detction).start()