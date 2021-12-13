(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (sign val)
    (
        cond
            ((< val 0) -1)
            ((= val 0) 0)
            (else 1)
    )
)

(define (square x) (* x x))

(define (pow base exp)
    (if(= 1 exp)
            base
            (if(even? exp) 
                ; let (a (pow base (/ exp 2))) (* a a)               
                (let(
                    (a (pow base (/ exp 2)))
                    )
                    (* a a)
                )
                (* base (pow base (- exp 1)))
            )
    )

)

(let ((x 5) (y (+ x 2))) (+ x y))