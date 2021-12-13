(define (replicate x n)
    (cond
        ((= n 1) (cons x nil))
        (#t (cons x (replicate x (- n 1))))
    )
)

;;; Tests
(replicate 5 3)
; expect (5 5 5)
