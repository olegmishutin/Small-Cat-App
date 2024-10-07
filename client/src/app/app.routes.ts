import { Routes } from '@angular/router';
import {LoginComponent} from './login/login.component';
import {RegisterComponent} from './register/register.component';
import {MenuComponent} from './menu/menu.component';
import {CreationComponent} from './creation/creation.component';

export const routes: Routes = [
  {
    path: 'login', component: LoginComponent
  },
  {
    path: 'register', component: RegisterComponent
  },
  {
    path: '', component: MenuComponent
  },
  {
    path: 'creation', component: CreationComponent
  },
  {
    path: 'cat/:id', component: CreationComponent
  }
];
