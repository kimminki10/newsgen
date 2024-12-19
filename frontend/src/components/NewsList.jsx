import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link, useParams } from "react-router-dom";
import "./NewsList.css";
import NewsItem from "./NewsItem";

const NewsList = () => {
  const {ticker} = useParams();
  const [tickerData, setTickerData] = useState({});
  const [articles, setArticles] = useState([]);
  useEffect(() => {
    const fetchTickerData = async () => {
      try {
        const response = await axios.get(`/api/ticker/${ticker}/`);
          const { articles, ...rest } = response.data;
          setTickerData(rest);
          setArticles(articles);
        } catch (error) {
          console.error("Error fetching ticker data:", error);
        }
      };
      fetchTickerData();
  }, []);

  return (
    <div className="news-list">
      <div className="ticker-info">
        <div className="ticker-title">{ticker}</div>
        <div>{tickerData.last_price}</div>
      </div>

      {articles.length !== 0 ?
      articles.map((news) => (
        <NewsItem
                    key={news.id}
                    title={news.title}
                    ticker={ticker}
                    date={tickerData.updated_at}
                    currentPrice={tickerData.last_price}
                    pricePointChange={tickerData.percentage_diff}
                    priceChange={tickerData.price_diff}
                    content={news.content}
                />
      ))
      : 
      <p>No news found for this ticker</p>}
    </div>
  );
};

export default NewsList;
