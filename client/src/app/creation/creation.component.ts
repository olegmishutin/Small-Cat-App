import {Component, AfterViewInit} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {ActivatedRoute} from '@angular/router';
import {showErrorFromResponse, hideError, showDetailErrorFromResponse} from '../../utils/shortcuts';
import axios from 'axios';

@Component({
  selector: 'app-creation',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './creation.component.html',
  styleUrls: ['../../styles/form_style.css', './creation.component.css']
})
export class CreationComponent implements AfterViewInit {
  id: string | null = null;

  name: string = ''
  age: any = null
  breed: string = ''
  color: string = ''
  favorite_food: string = ''

  constructor(private route: ActivatedRoute) {
  }

  ngAfterViewInit() {
    this.route.paramMap.subscribe(params => {
      this.id = params.get('id');
      if (this.id) {
        axios({
          method: 'GET',
          url: `/api/cats/${this.id}/`
        }).then((response) => {
          if (response.status === 200) {
            this.name = response.data.name
            this.age = response.data.age
            this.breed = response.data.breed
            this.color = response.data.color
            this.favorite_food = response.data.favorite_food
          }
        }).catch((error) => {
          if (error.response.status === 403) {
            window.location.href = '/'
          }
        })
      } else {
        axios({
          method: 'GET',
          url: '/api/me/'
        }).then((response) => {
          return null
        }).catch((error) => {
          if (error.response.status === 403) {
            window.location.href = '/'
          }
        })
      }
    });
  }

  action() {
    hideError([
      'name',
      'age',
      'breed',
      'color',
      'favorite_food',
      'detail',
    ])

    const formData = new FormData()
    formData.append('name', this.name)
    formData.append('age', this.age)
    formData.append('breed', this.breed)
    formData.append('color', this.color)
    formData.append('favorite_food', this.favorite_food)

    axios({
      method: this.id ? 'PUT' : 'POST',
      url: this.id ? `/api/cats/${this.id}/` : '/api/cats/',
      data: formData,
      xsrfCookieName: 'csrftoken',
      xsrfHeaderName: 'X-CSRFToken',
      withCredentials: true
    }).then((response) => {
      if (response.status === 201 || response.status === 200) {
        window.location.href = '/'
      }
    }).catch((error) => {
      if (error.response.status === 403) {
        window.location.href = '/'
      }
      showErrorFromResponse(error.response.data)
      showDetailErrorFromResponse(error.response.data, 'detail_error')
    })
  }
}
