import {Component} from '@angular/core';
import {hideError, showErrorFromResponse, showDetailErrorFromResponse} from '../../utils/shortcuts';
import axios from 'axios';
import {FormsModule} from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './login.component.html',
  styleUrl: '../../styles/form_style.css'
})
export class LoginComponent {
  username: string = ''
  password: string = ''

  login() {
    hideError([
      'username',
      'password'
    ])

    const data = {
      username: this.username,
      password: this.password
    }

    axios({
      method: 'POST',
      url: '/api/log/',
      data: data,
      xsrfCookieName: 'csrftoken',
      xsrfHeaderName: 'X-CSRFToken',
      withCredentials: true
    }).then((response) => {
      if (response.status === 200) {
        window.location.href = '/'
      }
    }).catch((error) => {
      showErrorFromResponse(error.response.data)
      showDetailErrorFromResponse(error.response.data, 'detail_error')
    })
  }
}
