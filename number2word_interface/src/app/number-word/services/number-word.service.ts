import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class NumberWordService {

  constructor(private http: HttpClient) {}

  getWordForNumber(wordNumber: number) {
    return this.http.get<string>(
      environment.apiBaseUrl + wordNumber
    );
  }
}
