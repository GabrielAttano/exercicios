import * as S from './styled'
import logo from '../../assets/logo.svg'
import { FaSearch } from "react-icons/fa";


function Header() {

  return (
    <S.Header className='header__container'>

      <div className='header__logo-container'>
        <a className='header' href='https://www.juntossomosmais.com.br/'>
          <img src={logo}/>
        </a>
      </div>

      <S.Nav className='header__nav'>
        <ul className='header__nav__ul'>

          <li className='header__nav_li'>
            <form>
              <S.InputWrapper className='input__wrapper'>
                <div className='input__icon'>
                  <FaSearch size={'19px'}/>
                </div>
                <div>
                  <input className='input' type={'text'} placeholder='Buscar aqui' />
                </div>
              </S.InputWrapper>
            </form>
          </li>

          <li className='header__nav_li'>test</li>

          <li className='header__nav_li'>test</li>

        </ul>
      </S.Nav>

    </S.Header>
  )
}

export default Header