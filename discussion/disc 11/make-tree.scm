(define (make-tree label branches) (cons label branches))

(define (label tree)
    (if (eqv? tree nil) nil 
        (car tree)
    )
)

(define (branches tree)
    (if (eqv? tree nil) nil 
        (cdr tree)
    )
)
