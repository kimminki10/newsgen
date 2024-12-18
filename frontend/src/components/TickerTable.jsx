import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCheck, faTimes } from "@fortawesome/free-solid-svg-icons";

const TickerTable = ({ data }) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>Ticker</th>
                    <th>Company</th>
                    <th>Price</th>
                    <th>Market Cap</th>
                    <th>Subscribed</th>
                </tr>
            </thead>
            <tbody>
                {data.map((row, index) => (
                    <tr key={index}>
                        <td>{row.ticker}</td>
                        <td>{row.company}</td>
                        <td>{row.price}</td>
                        <td>{row.marketCap}</td>
                        <td>
                            {row.subscribed ? (
                                <FontAwesomeIcon icon={faCheck} />
                            ) : (
                                <FontAwesomeIcon icon={faTimes} />
                            )}
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default TickerTable;