import React, { useRef, useState, useEffect } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearch } from "@fortawesome/free-solid-svg-icons";
import { useNavigate } from "react-router-dom";
import './SearchTextBox.css';
import axios from "axios";
import { useTicker } from "./TickerContext";

const SearchTextBox = ({ type, placeholder, value }) => {
    const searchRef = useRef(null);
    const [searchText, setSearchText] = useState('');
    const [suggestions, setSuggestions] = useState([]);
    const navigate = useNavigate();
    const { tickerList } = useTicker();

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
        // 첫 번째 suggestion을 선택하고, 해당 ticker의 detail page로 이동
        if (suggestions.length > 0) {
            navigate(`/ticker/${suggestions[0].ticker_name}`);
            searchRef.current.value = '';
            setSuggestions([]);
        }
    }

    const handleItemClick = (e) => {
        const tickerName = e.target.innerText;
        navigate(`/ticker/${tickerName}`);
        searchRef.current.value = '';
        setSuggestions([]);
    }

    return (
        <div className='search-text-box-container'>
            <div className='search-text-box'>
                <input 
                    ref={searchRef}
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
                        <li key={ticker.id} onClick={handleItemClick}>{ticker.ticker_name}</li>
                    ))
                }
                </ul>
            )}
                
        </div>
    );
}

export default SearchTextBox;