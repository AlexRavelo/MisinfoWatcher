import * as React from "react";
import './App.css';

function SearchResults(props) {
return (
<div>
    <a href="/"><svg className="search-results-logo"></svg></a>
    <div className="search-result-box">
        <div>
            <div>
                <h1>
                    MisinfoWatcher believes the article text is: {props.stateContext.searchResults.get.article_sentiment} 
                    with a confidence of {props.stateContext.searchResults.get.article_confidence}%
                </h1>
            </div>
                
            <div>
                <h1>
                    MisinfoWatcher believes the article title is: {props.stateContext.searchResults.get.title_sentiment} 
                    with a confidence of {props.stateContext.searchResults.get.title_confidence}%
                </h1>
            </div>

            <div>
                <ul>
                    {
                        props.stateContext.searchResults.get.entities.map(entity => (
                        <li>{entity}</li>
                        ))
                    }
                </ul>
            </div>
        </div>
    </div>
</div>
);
}

export default SearchResults;
