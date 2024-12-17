import React from 'react';
import NewsItem from './NewsItem';
import './AboutPage.css';

const fake_contents = [
    {
        id: 1,
        title: "Apple Inc. (AAPL) stock rises 5% in a day",
        ticker: "AAPL",
        priceChange: "+5%",
        currentPrice: "$145.09",
        pricePointChange: "+$6.91",
        date: "2024.10.01"
    },
    {
        id: 2,
        title: "Tesla Inc. (TSLA) stock falls 3% in a day",
        ticker: "TSLA",
        priceChange: "-3%",
        currentPrice: "$775.22",
        pricePointChange: "-$23.98",
        date: "2024.10.01"
    },
    {
        id: 3,
        title: "Amazon.com Inc. (AMZN) stock rises 2% in a day",
        ticker: "AMZN",
        priceChange: "+2%",
        currentPrice: "$3284.72",
        pricePointChange: "+$64.32",
        date: "2024.10.01"
    },
    {
        id: 4,
        title: "Microsoft Corporation (MSFT) stock rises 1% in a day",
        ticker: "MSFT",
        priceChange: "+1%",
        currentPrice: "$289.67",
        pricePointChange: "+$2.87",
        date: "2024.10.01"
    },
    {
        id: 5,
        title: "Meta Platforms Inc. (META) stock falls 4% in a day",
        ticker: "META",
        priceChange: "-4%",
        currentPrice: "$341.34",
        pricePointChange: "-$14.21",
        date: "2024.10.01"
    }
];

const fake_content = `웨드부시가 테슬라의 목표주가를 400달러에서 515달러로 상향 조정했다. 트럼프 행정부의 우호적인 규제 환경이 테슬라의 자율주행 및 AI 계획에 긍정적으로 작용할 것이라는 분석이다. 웨드부시는 테슬라에 대한 '아웃퍼폼' 등급을 유지하며, 단순한 자동차 회사가 아닌 혁신 기술 기업으로서의 가치를 강조했다.​웨드부시는 보고서에서 테슬라가 2025년 말까지 시가총액 2조 달러에 도달할 가능성을 제시했다. 완전자율주행(FSD) 기술 발전과 중국 시장의 강력한 수요가 성장을 견인할 것이라는 전망이다. 특히 FSD 기술의 침투율이 50%를 넘어서면서 테슬라의 재무 모델과 마진에 획기적인 변화를 가져올 것으로 예상하며, "테슬라 스토리에서 1조 달러의 AI 가치가 열리기 시작할 것"이라고 언급했다.​ 중국 관세 논의에 대한 테슬라의 전략적 참여 역시 지정학적 리스크 완화와 중국 시장 성장에 기여할 것으로 내다봤다. 생산 병목 현상이나 자본 조달과 같은 잠재적 어려움에도 불구하고, 웨드부시는 자율주행 및 AI 분야에서 테슬라의 장기적인 전망에 대해 낙관적인 입장을 유지했다. 테슬라는 현재 435.75달러에 거래되어 전일 종가 대비 0.11% 하락했다.`;

const TodaysNews = ({contents}) => {
    return (
        <div>
            <h1>💵 오늘의 핀트렌드</h1>
            {contents.map((content) => (
                <NewsItem
                    key={content.id}
                    title={content.title}
                    ticker={content.ticker}
                    date={content.date}
                    currentPrice={content.currentPrice}
                    pricePointChange={content.pricePointChange}
                    priceChange={content.priceChange}
                />
            ))}
        </div>
    );
}

const AboutPage = () => {
    return (
        <div>
            <h1>핀트렌드로 쉽게<br/>미국주식 뉴스기사를<br/>읽기 시작하세요.</h1>
            <p>관심있는 종목 선택만 하면<br/>관련 영어 뉴스를<br/><br/>한국어로 번역 및 요약해서<br/><br/>📧 매일 메일로!<br/><br/>🔉 출근길 읽어주는 뉴스!</p>
            <TodaysNews contents={fake_contents}/>
        </div>
    );
};

export default AboutPage;