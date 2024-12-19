import React, { useState, useEffect } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearch } from "@fortawesome/free-solid-svg-icons";
import './SearchTextBox.css';
import axios from "axios";

const SearchTextBox = ({ type, placeholder, value }) => {
    const [searchText, setSearchText] = useState('');
    const [tickerList, setTickerList] = useState([]);
    const [suggestions, setSuggestions] = useState([]);

    useEffect(() => {
        const fetchSearchResults = async () => {
            try {
                const response = await axios.get(`/api/ticker/`);
                setTickerList(response.data.tickers);
            } catch (error) {
                console.error(error);
            }
        }
        fetchSearchResults();
    }, []);

    useEffect(() => {
        if (searchText === '') {
            setSuggestions([]);
            return;
        }
        const filteredTickers = tickerList.filter((ticker) => {
            return ticker.ticker_name.toLowerCase().includes(searchText.toLowerCase());
        });
        setSuggestions(filteredTickers.slice(0, 10));
    }, [searchText]);

    const handleSearch = (e) => {
        setSearchText(e.target.value);
    }

    const handleKeyDown = (e) => {
        if (e.key !== 'Enter') { return; }
        console.log('Enter key pressed');
    }
    return (
        <div className='search-text-box-container'>
            <div className='search-text-box'>
                <input 
                    className="search-input"
                    type={type} 
                    placeholder={placeholder} 
                    value={value} 
                    onChange={handleSearch} 
                    onKeyDown={handleKeyDown}
                />
                <button className="search-button">
                    <FontAwesomeIcon icon={faSearch} />
                </button>
            </div>
            {suggestions && suggestions.length > 0 && (
                <ul className='suggestions-list'>
                {suggestions.slice(0, 10).map((ticker) => (
                        <li key={ticker.id}>{ticker.ticker_name}</li>
                    ))
                }
                </ul>
            )}
                
        </div>
    );
}

export default SearchTextBox;