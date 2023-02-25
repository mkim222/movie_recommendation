######################################
# 파이썬 streamlit를 통해서 웹사이트 만들기
# 출처 : https://youtu.be/TNcfJHajqJY
######################################


# 주피터 노트북에서 pickle 통해서 덤핑했던거 가져오기
import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb

movie = Movie()  # 객체생성
tmdb = TMDb()    # 객체생성
tmdb.api_key = '044f7463549ad12045282b83acbc0115'   # 서버끼리 연결해주기위해서 api키 입력 (api키는 tmdb웹사이트에서 로그인 후 확인가능)
# tmdb.language = 'ko-KR' # 한국어 버전


# get_recommendations 함수만들기
def get_recommendations(title):
    # 영화 제목을 통해서 전체 데이터 기준 그 영화의 index 값을 얻기
    idx = movies[movies['title'] == title].index[0]

    # 코사인 유사도 매트릭스 (cosine_sim) 에서 idx 에 해당하는 데이터를 (idx, 유사도) 형태로 얻기
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 코사인 유사도 기준으로 내림차순 정렬
    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)
    
    # 자기 자신을 제외한 10개의 추천 영화를 슬라이싱
    sim_scores = sim_scores[1:11]
    
    # 추천 영화 목록 10개의 인덱스 정보 추출
    movie_indices = [i[0] for i in sim_scores]
    
    # 인덱스 정보를 통해 영화 제목 추출
    images = []
    titles = []
    for i in movie_indices:
        id = movies['id'].iloc[i]
        details = movie.details(id)
        
        image_path = details['poster_path']
        if image_path:
            image_path = 'https://image.tmdb.org/t/p/w500' + image_path
        else:
            image_path = '/Users/minsookim/Desktop/Programming Language/Python/Machine Learning/Project/no_image.jpg'

        images.append(image_path)
        titles.append(details['title'])

    return images, titles


# pickle에서 덤핑했던거 가져오기
# rb : 읽기모드
movies = pickle.load(open('movies.pickle', 'rb'))
cosine_sim = pickle.load(open('cosine_sim.pickle', 'rb'))


# 웹사이트 디자인하기
st.set_page_config(layout = 'wide')
st.header('Minsooflix')
movie_list = movies['title'].values

title = st.selectbox('Choose a movie you like', movie_list)
# Recommend 버튼이 실행이되면 아래코드들이 동작한다!
if st.button('Recommend'):
    with st.spinner('Please wait...'):
        images, titles = get_recommendations(title)

        idx = 0
        for i in range(0, 2):
            cols = st.columns(5)        # 컬럼 5개 만들기
            for col in cols:
                col.image(images[idx])  # 이미지 보여주기
                col.write(titles[idx])  # 제목 보여주기
                idx += 1                    