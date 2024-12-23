import React, { useState, useEffect } from "react";
import NewsItem from "./NewsItem";
import "./AboutPage.css";
import { useAuth } from "./AuthContext";
import axios from "axios";

const TodaysNews = ({ contents, tickers }) => {
  return (
    <div>
      <h1>💵 오늘의 핀트렌드</h1>
      {contents.map((content) => {
        let ticker = tickers.find((ticker) => ticker.ticker_name === content.tickers[0]);
        if (!ticker) {
          ticker = {};
          ticker.ticker_name = content.tickers[0];
          ticker.updated_at = "-";
          ticker.last_price = "-";
          ticker.price_diff = "-";
          ticker.percentage_diff = "-";
        }

        return <NewsItem
          key={content.id}
          title={content.title}
          ticker={ticker.ticker_name}
          date={ticker.updated_at}
          currentPrice={ticker.last_price}
          pricePointChange={ticker.price_diff}
          priceChange={ticker.percentage_diff}
          origin_url={content.origin_url}
          tts_url={content.tts_url}
          content={content.content}
        />
      })}
    </div>
  );
};

const AboutPage = () => {
  const [articles, setArticles] = useState([]);
  const [tickers, setTickers] = useState(null);

  const fetchArticles = async () => {
    try {
      const response = await axios.get("/api/article/");
      setArticles(response.data.results);
    } catch (error) {
      console.error("Error fetching articles:", error);
    }
  };

  const fetchTicker = async () => {
    try {
      const response = await axios.get(`/api/ticker/`);
      setTickers(response.data.tickers);
    } catch (error) {
      console.error("Error fetching ticker:", error);
    }
  }

  useEffect(() => {
    fetchArticles();
    fetchTicker();
  }, []);

  return (
    <div>
      <h1>
        핀트렌드로 쉽게
        <br />
        미국주식 뉴스기사를
        <br />
        읽기 시작하세요.
      </h1>
      <p>
        관심있는 종목 선택만 하면
        <br />
        관련 영어 뉴스를
        <br />
        <br />
        한국어로 번역 및 요약해서
        <br />
        <br />
        📧 매일 메일로!
        <br />
        <br />
        🔉 출근길 읽어주는 뉴스!
      </p>
      {(articles.length === 0 || tickers === null) ? <p>Loading...</p>
      : <TodaysNews contents={articles} tickers={tickers} />}
      
    </div>
  );
};

export default AboutPage;
