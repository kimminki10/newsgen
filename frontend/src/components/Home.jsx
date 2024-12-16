import React from "react";
import Header from "./Header";
import NewsList from "./NewsList";
import { Link } from "react-router-dom";
import SearchTextBox from "./SearchTextBox";
import "./Home.css";

const Home = () => {
  return (
    <div className="home">
      <h1>Welcome to the Home Page</h1>
      <div className="content">
        <div className="subscription-section">
          <div className="subscription-ticker">
            <Link to="/subscription">Subscription ticker</Link>
          </div>
          <NewsList />
        </div>
        <div className="all-section">
          <SearchTextBox type="text" placeholder="Search for ticker" />
          <NewsList />
        </div>
      </div>
    </div>
  );
};

export default Home;
