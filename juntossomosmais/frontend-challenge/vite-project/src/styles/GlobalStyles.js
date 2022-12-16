import styled, { createGlobalStyle } from 'styled-components'
import RobotoWoff from '../fonts/Roboto.woff'
import RobotoWoff2 from '../fonts/Roboto.woff2'

import * as C from '../config/colors'


export default createGlobalStyle`

  * {
      margin: 0;
      padding: 0;
      outline: none;
      box-sizing: border-box;
      font-family: 'Roboto';
      color: ${C.black};
  }
  
  html, body, #root {
    height: 100%;
  }

  button {
    cursor: pointer;
    background: none;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    font-weight: 700;
  }
  
`;
