import {Component, AfterViewInit} from '@angular/core';
import {CommonModule} from '@angular/common';
import axios from 'axios';

@Component({
  selector: 'app-menu',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './menu.component.html',
  styleUrl: './menu.component.css'
})
export class MenuComponent implements AfterViewInit {
  data: any[] = []

  ngAfterViewInit() {
    this.getData()
  }

  private getData() {
    axios({
      method: 'GET',
      url: '/api/cats/',
    }).then((response) => {
      if (response.status === 200) {
        this.data = response.data
      }
    }).catch((error) => {
      if (error.response.status === 403) {
        window.location.href = '/login/'
      }
    })
  }

  delete(id: any) {
    axios({
      method: 'DELETE',
      url: `/api/cats/${id}/`,
      xsrfCookieName: 'csrftoken',
      xsrfHeaderName: 'X-CSRFToken',
      withCredentials: true
    }).then((response) => {
      if (response.status === 204) {
        this.getData()
      }
    }).catch((error) => {
      this.getData()
    })
  }
}
