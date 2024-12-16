import React from "react";
import SearchTextBox from "./SearchTextBox";


const TodaysNewsItem = ({ title, content, ticker,  }) => {
    return (
        <div>
            <h3>{ticker}</h3>
            <p>{title}</p>
            <p>{content}</p>
        </div>
    );
};

const TodaysNews = () => {
    return (
        <div>
            <h2>오늘의 뉴스</h2>
            <div>
                <h3>삼성전자</h3>
                <p>삼성전자가 5G 스마트폰 갤럭시S22를 출시했다. 이 제품은 전작인 갤럭시S21보다 5G 통신 속도가 빨라졌다.</p>
            </div>
            <div>
                <h3>애플</h3>
                <p>애플이 새로운 맥북 프로를 출시했다. 이 제품은 기존 맥북 프로보다 성능이 2배 빨라졌다.</p>
            </div>
        </div>
    );
}

const AboutPage = () => {
    return (
        <div>
            <h1>핀트렌드로 쉽게<br/>미국주식 뉴스기사를<br/>읽기 시작하세요.</h1>
            <SearchTextBox type="text" placeholder="심볼 또는 회사이름으로 검색" value="" onChange={() => {}} />
            <p>관심있는 종목 선택만 하면<br/>해당종목 관련 영어 뉴스를<br/>한국어로 번역 및 요약해서 매일 메일로!<br/>출근길 읽어주는 뉴스!</p>
            <TodaysNews />
        </div>
    );
};

export default AboutPage;