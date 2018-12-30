오픈 소스 SW입문 7조 Team Project
==========================================

## 1. 프로젝트 이름
------------------

### : Predict_Lol_Winning_Rate

## 2. 팀멤버
-------------------------

|이름|역할|
|----|:----|
|이정은|README 제작, crawling|
|이다운|README 제작, 오픈소스 기능 수정 및 개선, 알고리즘|
|김동현|README 제작, FrontEnd|
|최지원|README 제작, 오픈소스 기능 수정 및 개선, |


## 3. 프로그램 선정 배경 및 목적
------------------
### 3-1. 프로그램 선정 배경

* League of Legend라는 게임은 세계 최고의 MOBA(Multiplayer Online Battle Arena) 게임이다. 10명의 유저가 5:5로 맞붙는 게임이기 때문에 협동과 전략이 중요하다. 현재 League of Legend는 전세계 게임시장 점유율1위이고, 프로게이머들이 활동할 수 있도록 프로구단도 존재한다. 또한, Top급 프로게이머의 연봉이 수십억이 될 정도로 인기가 많은 게임이다. 저희 팀은 이 게임의 전략과 승률을 예측하기 어렵다는 면에서 많은 게임 사용자들에게 승률을 대신 예측해주고자 프로젝트를 시작하게 되었다.

### 3-2. 프로그램 목적

* 자주 업데이트 되는  _League of Legends_ 의 특성상 업데이트 내용에 따라 Champion간의 상성이 바뀔 수 있다.

* Champion간의 승률을 종합하여 전체 게임의 승률을 도출해낸다.

## 4. 프로젝트 내용
------------------
### 4-1. 기능설명
* 온라인 게임 _League of Legends_ 에서 게임 승률 예측, 분석 기능
* op.gg라는 사이트에서 제공해주는 챔피언 간의 승률 정보를 crawling을 통해 추출해온다.
* 추출한 챔피언 간의 승률 정보를 알고리즘을 통해 팀의 승률을 도출해낸다.

### 4-2. Crawling
* op.gg
![alt text][1]
[1]: /opgg.PNG

* Crawling 오픈소스
![alt text][2]
[2]: /crawlingopen.png

* Crawling 오픈소스 예제를 이용하여 op.gg에서 제공하는 챔피언 간의 승률 정보를 Crawling하여 추출하였다.

* op.gg에서 crawling하는 코드
![alt text][8]
[8]: /mycrawl.PNG


### 4-3. 사용한 프레임 워크
![alt text][3]
[3]: /webapp1.png

* Django는 파이썬으로 만들어진 무료 오픈소스 웹 애플리케이션 프레임워크로, 쉽고 빠르게 웹사이트를 개발할 수 있도록 돕는 구성요소로 이루어진 웹 프레임 워크이다.

* 본 프로젝트는 오픈소스인 Django를 이용하여 로컬 서버를 만들었고, 사용자는 해당 서버에서 프로그램을 실행시킬 수 있다. 이 프레임워크를 사용하여 index.html(FrontEnd)에서 request요청을 보내면 predict.py(BackEnd)에서 일련의 계산과정을 거친 뒤에 request에 대한 답으로 respond를 보내게 된다.

![alt text][9]
[9]: /request.png

* index.html에서 전송 요청을 누르면 입력된 챔프의 데이터들이 team_a, team_b에 들어가게 된다.

![alt text][10]
[10]: /respond.png

* team_a, team_b 데이터를 predict.py의 parameter로 넣는다. 그 결과값을 다시 data라는 구조 안의 team1, team2에 넣게 되며 이 data는 render()를 통해 html에서 보여지게 된다.

### 4-6 전체적 시스템 구조

* 클라이언트(크롬), 웹 서버, App 서버 구조로 이뤄지도록 했다.

* Html, css, javaScript, python, Django를 채택하여 활용했다.

### 4-5. 부족한 기능 파악후, 기능 개선 목록
* 기존 승률 예측 프로그램에 대한 오픈소스는 아직 완성되지 않은 프로그램이었고, 유저들의 챔피언 숙련도를 바탕으로 승률을 예측.
* 기존 프로그램에서 Champion별 승률까지 고려하여 조금 더 정확한 승률을 예측 가능하게 구현.

### 4-6. 이 프로젝트로 무엇이 달라지고, 개선되는지, 누구에게 benefit을 주는지 명확하게 명시할 것
* 기존 미완성된 오픈소스에 대해 기여를 통해 SW개발자에게 도움
* 웹 어플리케이션을 통해 일반 사용자들도 활용할 수 있도록 함

## 5. 프로그램 시뮬레이션
-----------------------
### 5.1 **챔피언 입력 전**

![alt text][5]
[5]: /simulation_1.PNG

* 승리 결과가 눈에 보이지 않는다. (챔피언 값을 입력하고 전송을 눌러야만 보임)

### 5.2 **챔피언 입력 후**

![alt text][11]
[11]: /simulation_2.PNG

* 아군 팀과 적 팀 각각에 대한 승률과 챔피언 목록이 출력된다.

### 5.3 **승률 알고리즘**
* 각 라인별 Champion끼리의 승률을 op.gg에서 크롤링하여 가져온다.
* League of Legend의 게임 특성상 매번 강한 라인과 약한 라인이 존재하며 현재는 Mid와 Jungle이 강한
상황을 고려하여 두 라인에 좀 더 비중을 두었다. 그리고 Bottom라인이 약한 상황이기에 나머지 라인들에 비해 조금 비중을 낮추었다.
* 결과적으로 Top 라인에 20%, Jungle과 Mid 라인에 각각 30%, Bottom 라인에 각각 10%씩 비중을 두었으며 이 모든 값을 합산하여 팀 승률을 계산한다.


## 6. 사용되는 Github 오픈소스 SW 목록
------------------------------------

* *https://github.com/crosstreet74/blog-date2num-crawler/blob/master/blog-date2num-crawler.py*

  => crawling을 위함

* *https://github.com/Najsr/League-Of-Legends-Champions-ID-List*

  => Champion 이름과 ID를 matching

* *https://github.com/arilato/ranked_prediction/*

  => 현재 진행중인 승률 예측 프로그램

* *https://github.com/django/django*

  =>파이썬으로 만들어진 무료 오픈소스 웹 애플리케이션 프레임워크

## 7. 이 작업 이후, 추가적으로 진행되면 좋은 작업들
-------------------------------------------------------

* UI 개선을 위하여 CSS를 작성
* 각 라인마다 입력되는 챔피언의 종류에 제한을 둔다.
* 챔피언 조합의 시너지를 고려하여 팀의 승률 예측 기능을 개선한다.
  => *https://www.leagueofgraphs.com/ko/champions/counters*

* 유저의 실력 점수(rating)을 가져와 승률 예측에 반영
* 최근 전적을 고려하여 승률 예측에 반영.
* 유저들의 의견을 참고하기 위해 따로 코멘트 기능 추가.
* 현재는 랭크게임에 한해서 승률계산을 제공하지만, 일반 게임에 대한 승률계산을 추가한다.
* 현재 op.gg에서 챔피언간의 승률만을 보여주지만, 좀 더 알고리즘을 구체화하여 op.gg에서 팀간의 승률또한
  보여주는것을 건의해볼 생각이다.


## 8. 라이센스
-------------------------------------------------------
* Apache License 2.0 *http://www.apache.org/licenses/*
* MIT License *https://github.com/crosstreet74/blog-date2num-crawler/blob/master/LICENSE*
