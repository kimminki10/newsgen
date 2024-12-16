import React from "react";
import { Link } from "react-router-dom";
import { list } from "../data/newsList";
import "./NewsList.css";

const NewsList = () => {
  return (
    <div className="news-list">
      {list.map((news) => (
        <div key={news.id} className="news-item">
          <h2>{news.title}</h2>
          <p>{news.summary}</p>
          <Link to={`/summary/${news.id}`}>Read more</Link>
        </div>
      ))}
    </div>
  );
};

export default NewsList;
