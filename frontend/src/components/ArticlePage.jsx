import React from "react";
import NewsList from "./NewsList";

const ArticlePage = ({ticker}) => {
    return (
        <div>
            <h1>Articles</h1>
            <NewsList />
        </div>
    );
}