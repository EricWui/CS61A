(define (map fn lst)
    (cond
        ((eqv? lst nil) nil)
        (#t (cons (fn (car lst)) (map fn (cdr lst))))
    )
)

;;; Tests
(map (lambda (x) (* x x)) '(1 2 3))
; expect (1 4 9)
