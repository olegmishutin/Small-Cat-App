import {Component, AfterViewInit} from '@angular/core';
import {FormsModule} from '@angular/forms';
import axios from 'axios';
import {NgForOf} from '@angular/common';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [FormsModule, NgForOf],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.css'
})
export class ChatComponent implements AfterViewInit {
  username: string = ''
  messages: any = []
  socket: WebSocket | null = null

  inputMessage: string = ''

  ngAfterViewInit() {
    axios({
      method: 'GET',
      url: '/api/me/'
    }).then((response) => {
      this.username = response.data.username
    }).catch((error) => {
      if (error.response.status === 403) {
        window.location.href = '/login/'
      }
    })

    this.socket = new WebSocket('ws://localhost:8000/ws/chat/')
    this.socket.onmessage = (event) => {
      const data = JSON.parse(event.data)

      if (data instanceof Array) {
        this.messages = data
      } else {
        this.messages.push(data)
      }
    }

    type MutationCallback = (mutationsList: MutationRecord[], observer: MutationObserver) => void;
    const targetNode = document.getElementById('chat-scroll-element') as HTMLUListElement;

    if (targetNode) {
      const config: MutationObserverInit = {childList: true, subtree: true, attributes: true};

      const callback: MutationCallback = (mutationsList) => {
        mutationsList.forEach(mutation => {
          if (mutation.type === 'childList') {
            if (targetNode.scrollHeight - targetNode.scrollTop <= 1000) {
              targetNode.scrollTop = targetNode.scrollHeight
            }
          }
        });
      };
      const observer = new MutationObserver(callback);
      observer.observe(targetNode, config);
    }
  }

  send() {
    this.socket?.send(JSON.stringify({"message": this.inputMessage}))
    this.inputMessage = ''
  }
}
