import wave

Orignal = wave.open('OrignalAudiofileName.wav', 'r')
Converted = wave.open('ConvertedAudiofileName.wav.wav','r')

n = Orignal.getnframes()

wavedataO = Orignal.readframes(n)
wavedataC = Converted.readframes(n)

wavedataOc = Orignal.getparams()
wavedataCc = Converted.getparams()


if wavedataO==wavedataC:
    if wavedataOc==wavedataCc:
        print("files are identical")
else:
    print("files are not identical")


