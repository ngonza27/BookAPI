import {Component, OnInit, OnChanges} from '@angular/core';
import {Router} from '@angular/router';
import {BookService} from './book.service';
import {Book} from './book';

@Component({
    selector: 'app-book',
    templateUrl: './book.component.html',
    styleUrls: ['./book.component.css']
})
export class BookComponent implements OnInit, OnChanges{

    books: Book[];
    statusMessage: string;
    book = new Book();
    
    constructor(private _bookService: BookService,
                private _router: Router){}

    ngOnInit(): void {
        this.getBooks();
    }

    getBooks(): void{
        this._bookService.getAllBooks()
            .subscribe((bookData) => this.books = bookData,
            (error) =>{
                console.log(error);
                this.statusMessage = "Problem with service. Please try again later!";
            }
        );
    }

    addBook(): void{
        this._bookService.addBook(this.book)
            .subscribe((response) => {console.log(response); this.getBooks();this.reset();},
            (error) =>{
                console.log(error);
                this.statusMessage = "Problem with service. Please try again later!";
            }
        );           
    }

    private reset(){
        this.book.id = null;
        this.book.title = null;
        this.book.author = null;
    }

    ngOnChanges(changes:any) {
    }

    deleteBook(bookId: string){
        this._bookService.deleteBook(bookId)
            .subscribe((response) => {console.log(response); this.getBooks();},
            (error) =>{
                console.log(error);
                this.statusMessage = "Problem with service. Please try again later!";
            });
            this.reset();
    }

    getBook(bookId: string){
        this._bookService.updateBookById(bookId, this.book)
            .subscribe((bookData) => {this.book; this.getBooks(); }),
            (error) => {
                console.log(error);
                this.statusMessage = "Problem with service. Please try again later!";
            }
        this.reset();    
    }
}