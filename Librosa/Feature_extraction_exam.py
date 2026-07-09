# 특징 추출(feature extraction) 예제
import numpy as np
import librosa

# 예제 오디오 클립 불러오기
y, sr = librosa.load(librosa.ex('nutcracker'))

# hop_length 설정: 22050Hz 기준으로 512 샘플은 약 23ms에 해당
hop_length = 512

# 화성 성분(harmonic)과 타악기 성분(percussive)을 두 개의 파형으로 분리
y_harmonic, y_percussive = librosa.effects.hpss(y)

# 타악기 성분을 이용해 비트(박자) 트래킹
tempo, beat_frames = librosa.beat.beat_track(y=y_percussive,
                                             sr=sr)

# 원본 신호에서 MFCC(음색 특징) 계산
mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=13)

# MFCC의 1차 차분(델타 특징, 시간에 따른 변화량) 계산
mfcc_delta = librosa.feature.delta(mfcc)

# 특징들을 쌓고, 박자 이벤트에 맞춰 동기화(정리)
# 이번엔 (기본값인) 평균값을 사용
beat_mfcc_delta = librosa.util.sync(np.vstack([mfcc, mfcc_delta]),
                                    beat_frames)

# 화성 성분에서 크로마(음정/코드) 특징 계산
chromagram = librosa.feature.chroma_cqt(y=y_harmonic,
                                        sr=sr)

# 박자 이벤트 사이의 크로마 특징을 집계(요약)
# 여기서는 각 특징의 중앙값(median)을 사용
beat_chroma = librosa.util.sync(chromagram,
                                beat_frames,
                                aggregate=np.median)

# 마지막으로, 모든 박자 동기화 특징들을 하나로 합치기
beat_features = np.vstack([beat_chroma, beat_mfcc_delta])

