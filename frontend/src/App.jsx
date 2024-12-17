import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./components/Home";
import Login from "./components/Login";
import Register from "./components/Register";
import NewsList from "./components/NewsList";
import SummaryHome from "./components/summaryHome";
import SummarySubject from "./components/summarySubject";
import NewsTemplate from "./components/NewsTemplate";
import Subscription from "./components/Subscription";
import AboutPage from "./components/AboutPage";
import Layout from "./components/Layout";
import ResetPasswordPage from "./components/ResetPasswordPage";
import "./App.css";

function App() {
  return (
    <>
      <Router>
        <Layout>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/reset-password" element={<ResetPasswordPage />} />
            <Route path="/ticker/:ticker" element={<NewsList />} />
            <Route path="/register" element={<Register />} />
            <Route path="/news" element={<NewsList />} />
            <Route path="/news/template" element={<NewsTemplate />} />
            <Route path="/articles/:id" element={<SummarySubject />} />
            <Route path="/summary" element={<SummaryHome />} />
            <Route path="/summary/:id" element={<SummarySubject />} />
            <Route path="/about" element={<AboutPage />} />
            <Route path="/subscription" element={<Subscription />} />
          </Routes>
        </Layout>
      </Router>
    </>
  );
}

export default App;
