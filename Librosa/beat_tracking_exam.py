# Beat tracking exmaple
# 오디오 파일에서 박자(beat)를 자동으로 감지
import librosa

# 1. librosa에 내장된 예제 오디오 파일의 경로 가져오기
filename = librosa.example('nutcracker')

# 2. 오디오를 파형(waveform) 데이터 `y`로 불러오기
#    샘플링 레이트(sr, 1초당 샘플 개수)도 함께 저장
y, sr = librosa.load(filename)

# 3. 기본 비트 트래커(박자 감지기) 실행
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo[0]))

# 4. 감지된 박자의 프레임 번호를 실제 "시간(초)"으로 변환
beat_times = librosa.frames_to_time(beat_frames, sr=sr)