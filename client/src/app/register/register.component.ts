import {Component} from '@angular/core';
import axios from 'axios';
import {hideError, showErrorFromResponse} from '../../utils/shortcuts';
import {FormsModule} from '@angular/forms';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [
    FormsModule
  ],
  templateUrl: './register.component.html',
  styleUrl: '../../styles/form_style.css'
})
export class RegisterComponent {
  username: string = ''
  email: string = ''
  password: string = ''

  register() {
    hideError([
      'username',
      'email',
      'password'
    ])

    const data = {
      username: this.username,
      email: this.email,
      password: this.password
    }

    axios({
      method: 'POST',
      url: '/api/reg/',
      data: data,
      xsrfCookieName: 'csrftoken',
      xsrfHeaderName: 'X-CSRFToken',
      withCredentials: true
    }).then((response) => {
      if (response.status === 201) {
        window.location.href = '/login/'
      }
    }).catch((error) => {
      showErrorFromResponse(error.response.data)
    })
  }
}
