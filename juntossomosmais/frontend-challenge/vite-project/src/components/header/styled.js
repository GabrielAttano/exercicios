import styled from 'styled-components'

import * as C from '../../config/colors'

export const Header = styled.div`
  align-items: center;
  background-color: ${C.lighterGray};
  display: flex;
  justify-content: center;
  padding: 1.7em 9.5em;

  .header__logo-container {
    width: 92px;
  }

  @media (min-width: 992px) {
      justify-content: space-between;
      .header__logo-container {
        width: 148px;
      }
    }
`

export const Nav = styled.nav`
  
  display: none;

  .header__nav__ul {
    align-items: center;
    list-style: none;
    display: flex;
    justify-content: flex-end;
    gap: 16px;
  }

  .header__nav__li {
    margin: 0 1em;
  }
  
  @media (min-width: 992px) {
    display: flex;
  }
`

export const InputWrapper = styled.div`
  align-items: center;
  background-color: ${C.white};
  border: 1px solid ${C.lightGray};
  border-radius: 32px;
  display: flex;
  gap: 13px;
  height: 48px;
  justify-content: flex-start;
  padding: 19px 12px;
  width: 464px;

  .input {
    color: ${C.black};
    border: 0;
    font-size: 16px;
    outline: 0;
    width: 75%;
    ::placeholder {
      color: ${C.lightGray};
    }
  }
`
