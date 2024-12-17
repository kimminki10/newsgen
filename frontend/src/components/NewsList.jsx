import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link, useParams } from "react-router-dom";
import "./NewsList.css";
import config from "../config";

const NewsList = () => {
  const {ticker} = useParams();
  const [tickerData, setTickerData] = useState([]);
  useEffect(() => {
    const fetchTickerData = async () => {
      try {
        const response = await axios.get(`${config.backendBaseUrl}/article/${ticker}`);
            setTickerData(response.data);
        } catch (error) {
            console.error("Error fetching ticker data:", error);
        }
      };
      fetchTickerData();
  }, [ticker]);

  return (
    <div className="news-list">
      <div className="ticker-title">{ticker}</div>
      {tickerData.length === 0 ?
      tickerData.map((news) => (
        <div key={news.id} className="news-item">
          <h2>{news.title}</h2>
          <p>{news.summary}</p>
          <Link to={`/summary/${news.id}`}>Read more</Link>
        </div>
      ))
      : 
      <p>No news found for this ticker</p>}
    </div>
  );
};

export default NewsList;
