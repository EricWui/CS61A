(define (duplicate lst)
    (if (eqv? lst nil) nil
        (cons (car lst) (cons (car lst) (duplicate (cdr lst))))      
    )
)
