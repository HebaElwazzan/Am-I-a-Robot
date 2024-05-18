import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class HttprequestsService {
  url = "http://127.0.0.1:4091/"
  constructor(private _http : HttpClient) { }

  start_game() {
    return this._http.get(this.url + "start_game")
  }

  get_result(body : any) {
    return this._http.post(this.url + "get_result", body)
  }

  get_stats() {
    return this._http.get(this.url + "get_stats")
  }

}
