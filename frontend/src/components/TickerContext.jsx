import React, { createContext, useState, useEffect, useContext } from 'react';
import axios from 'axios';

const TickerContext = createContext();

export const TickerProvider = ({ children }) => {
    const [tickerList, setTickerList] = useState([]);

    useEffect(() => {
        const fetchTickers = async () => {
            try {
                const response = await axios.get(`/api/ticker/`);
                setTickerList(response.data.tickers);
            } catch (error) {
                console.error(error);
            }
        };
        fetchTickers();
    }, []);

    return (
        <TickerContext.Provider value={{ tickerList }}>
            {children}
        </TickerContext.Provider>
    );
};

export const useTicker = () => useContext(TickerContext);