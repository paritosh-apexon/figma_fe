import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Rating {
  userId: string;
  port: string;
  section: string;
  rating: number;
  comment?: string;
}

@Injectable({
  providedIn: 'root'
})
export class RatingService {
  private baseUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) {}

  getRating(userId: string, port: string, section: string): Observable<any> {
    return this.http.get(`${this.baseUrl}/ratings`, {
      params: { userId, port, section }
    });
  }

  submitRating(data: Rating): Observable<any> {
    return this.http.post(`${this.baseUrl}/ratings`, data);
  }
}