import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { Book } from './book';

@Injectable()
export class BookService{
    
    constructor(private _httpService: Http){}

    getAllBooks(): Observable<Book[]>{
        console.log("inside the service getAllBooks():::::::");
        return this._httpService.get("http://localhost:5000/book")
                .map((response: Response) => response.json())
                .catch(this.handleError);
    }

    getBookById(bookId: string): Observable<Book>{
        console.log("Inside the getBookById() service::::::");
        return this._httpService.get("http://localhost:5000/book/"+bookId)
                .map((response: Response) => response.json())
                .catch(this.handleError);
    }

    updateBookById(bookId: string, book: Book){
        let body = JSON.parse(JSON.stringify(book));
        let headers = new Headers({ 'Content-Type': 'application/json' });
        let options = new RequestOptions({ headers: headers });
        console.log("Inside the getBookById() service::::::");
        return this._httpService.put("http://localhost:5000/book/"+bookId, body, options);
    }
    
    addBook(book: Book){
        let body = JSON.parse(JSON.stringify(book));
        let headers = new Headers({ 'Content-Type': 'application/json' });
        let options = new RequestOptions({ headers: headers });
        console.log("Inside addBook add service():::::::");
        return this._httpService.post("http://localhost:5000/book", body, options);
    }

    deleteBook(bookId: string){
        console.log("Inside the service deleteBook():::::book id:::"+bookId);
        return this._httpService.delete("http://localhost:5000/book/"+bookId);
    }

    private handleError(error: Response){
        console.error(error);
        return Observable.throw(error);
    }
}