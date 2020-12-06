import * as React from "react";
import './App.css';
import { ListItem, ListItemLabel } from "baseui/list";
import {useStyletron} from 'baseui';
import {
    Card,
    StyledBody,
    StyledAction
  } from "baseui/card";
  import {FlexGrid, FlexGridItem} from 'baseui/flex-grid';



function SearchResults(props) {
const [css] = useStyletron();

const itemProps = {
    backgroundColor: 'mono300',
    height: 'scale1000',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  };

return (
<div>
    <a href="/"><svg className="search-results-logo"></svg></a>
    <div className="search-result-box">
        <FlexGrid
        flexGridColumnCount={3}
        flexGridColumnGap="scale800"
        flexGridRowGap="scale800"
        >
            <Card>
                <StyledBody>
                    MisinfoWatcher believes the article text is: {props.stateContext.searchResults.get.article_sentiment} 
                    with a confidence of {props.stateContext.searchResults.get.article_confidence}%
                </StyledBody>
            </Card>

            <Card>
                <StyledBody>
                    MisinfoWatcher believes the article title is: {props.stateContext.searchResults.get.title_sentiment}  
                    with a confidence of {props.stateContext.searchResults.get.title_confidence}%
                </StyledBody>
            </Card>

            <Card>
                <StyledBody>
                    Article Summary: {props.stateContext.searchResults.get.article_summary}
                </StyledBody>
            </Card>

            {
            props.stateContext.searchResults.get.entities.map(entity => (
            <Card>
                <StyledBody>Entity: {entity}</StyledBody>
            </Card>))
            }
        </FlexGrid>
    </div>
</div>
);
}

export default SearchResults;
