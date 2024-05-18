import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MatButton, MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { CommonModule } from '@angular/common';
import { HttprequestsService } from './services/httprequests.service';
import {MatProgressSpinnerModule} from '@angular/material/progress-spinner'; 

let material_modules = [
  MatButtonModule,
  MatIconModule,
  MatButton,
  MatProgressSpinnerModule
]

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, material_modules, CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  startGameClicked = false;
  paragraphText: string = '';
  resultsShowing = false;
  results : boolean | null = null;
  stats : any = null;

  constructor(private _http : HttprequestsService) {}

  startGame() {
    this.startGameClicked = true;
    // Fetch paragraph text from API
    this.fetchParagraphText();
  }

  fetchParagraphText() {
    this._http.start_game().subscribe({
      next: (data : any)=> {
        console.log(data)
        this.paragraphText = data.paragraph;
      },
      error: (error)=> {
        console.log(error)
      }
    })

  }

  get_result(answer : string) {
    let body = {'answer':answer}
    this._http.get_result(body).subscribe({
      next: (data : any) => {
        this.results = data.result;
        console.log(data)
        this.resultsShowing = true;
        this.startGameClicked = false;
        this.get_stats();
      },
      error: (error) => {
        console.log(error)
      }
    })
  }

  get_stats() {
    this._http.get_stats().subscribe({
      next: (data : any) => {
        this.stats = data
      }
    })
  }

  reset() {
    this.startGameClicked = false;
    this.paragraphText = '';
    this.resultsShowing = false;
    this.results = null;
  }

}
