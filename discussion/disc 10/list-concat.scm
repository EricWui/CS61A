(define (list-concat a b)
    
    (cond
        ((eqv? a nil) b)
        (#t (cons (car a) (list-concat (cdr a) b)))
    )
)
