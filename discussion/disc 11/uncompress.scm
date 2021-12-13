(define (uncompress s)
    (define (my-append a b)
        (if (null? a) b 
            (cons (car a) (my-append (cdr a) b))
        )
    )
    (define (replicate x n)
        (cond
            ((= n 1) (cons x nil))
            (#t (cons x (replicate x (- n 1))))
        )
    )
    (if (eqv? nil s) nil
        (my-append (replicate (car (car s)) (car (cdr (car s)))) (uncompress (cdr s)))
    )
)


;;; Tests
(uncompress '((a 4) (b 2) (c 3)))
; expect (a b b c c c)
