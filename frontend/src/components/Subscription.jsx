import React from "react";
import SearchTextBox from "./SearchTextBox";
import TickerTable from "./TickerTable";
import NewsList from "./NewsList";

const fakeNasdaqData = [
    { ticker: "AAPL", company: "Apple Inc.", price: 150.00, marketCap: "2.5T", subscribed: true },
    { ticker: "MSFT", company: "Microsoft Corp.", price: 280.00, marketCap: "2.1T", subscribed: false },
    { ticker: "GOOGL", company: "Alphabet Inc.", price: 2700.00, marketCap: "1.8T", subscribed: true },
    { ticker: "AMZN", company: "Amazon.com Inc.", price: 3400.00, marketCap: "1.7T", subscribed: false },
    { ticker: "FB", company: "Meta Platforms Inc.", price: 350.00, marketCap: "1.0T", subscribed: true },
    { ticker: "TSLA", company: "Tesla Inc.", price: 700.00, marketCap: "700B", subscribed: false },
    { ticker: "NVDA", company: "NVIDIA Corp.", price: 220.00, marketCap: "550B", subscribed: true },
    { ticker: "PYPL", company: "PayPal Holdings Inc.", price: 190.00, marketCap: "220B", subscribed: false },
    { ticker: "INTC", company: "Intel Corp.", price: 55.00, marketCap: "220B", subscribed: true },
    { ticker: "CSCO", company: "Cisco Systems Inc.", price: 60.00, marketCap: "250B", subscribed: false }
];

const Subscription = () => {
    return (
        <div>
            <h1>Subscription</h1>
            <SearchTextBox type="text" placeholder="Search for ticker" />
            <TickerTable data={fakeNasdaqData} />
            <NewsList />
        </div>
    );
};

export default Subscription;