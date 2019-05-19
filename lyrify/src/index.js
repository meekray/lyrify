import 'babel-polyfill';
import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App';
import { Provider } from 'react-redux';
import { ConnectedRouter } from 'connected-react-router';
import './assets/styles/style';

// render the main component
ReactDOM.render(
  <App/>,
  document.getElementById('app')
);