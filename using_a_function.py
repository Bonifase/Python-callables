# from twitter import (
#     tweet,
#     MessageTooLongError,
#     CommunicationError,
# )


message = "What would you like to tweetesrdtfyujikolserolp;['dftyikl;'dxfcgvhbjknlm;,'dxfcgvhbjknlm;,'dxfcgvhbjnklm,;dxfcgvhbjknl;?  "
# Your code here


try:
    len(message) <= 42
    print(message)
#     tweet(message)

# except CommunicationError:
#     print("An error occurred attempting to connect to Twitter. Please try again!")

except MessageTooLongError:
    print("Oh no! Your message was too long (...)")
