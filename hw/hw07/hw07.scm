(define (filter-lst fn lst)
  (cond
    ((eqv? lst nil) nil)
    ((fn (car lst)) (cons (car lst) (filter-lst fn (cdr lst))))
    (else (filter-lst fn (cdr lst)))
  )
)
; ;; Tests
(define (even? x) (= (modulo x 2) 0))


(filter-lst even? '(0 1 1 2 3 5 8))

; expect (0 2 8)
(define (interleave first second)
  (define (add first second index)
    (cond 
      ((eqv? first nil) second)
      ((eqv? second nil) first)
      (else
          (if (even? index)
            (cons (car second) (add first (cdr second) (+ index 1)))
            (cons (car first) (add (cdr first) second (+ index 1)))
          )
      )
    )
  )
  (add first second 1)
)

(interleave (list 1 5 3) (list 2 4 6))

; expect (1 2 5 4 3 6)
(interleave (list 1 3 5) nil)

; expect (1 3 5)
(interleave (list 1 3 5) (list 2 4))

; expect (1 2 3 4 5)
(define (accumulate combiner start n term)
  (define (accmulate_n combiner n term)
    (if (= 1 n) 1
      (combiner (term n) (accmulate_n combiner (- n 1) term))
    )
  )
  (combiner start (accmulate_n combiner n term))
)

(define (without-duplicates lst)
  (define (is-exit lst element)
    (cond
      ((eqv? lst nil) #f)
      ((= (car lst) element) #t)
      (else (is-exit (cdr lst) element))
    )
  )
  ; (define (duplicate ans lst)
  ;   (cond
  ;     ((eqv? lst nil) ans)
  ;     ((is-exit ans (car lst)) (duplicate ans (cdr lst)))
  ;     (else (duplicate (cons (car lst) ans) (cdr lst)))
  ;   )
  ; )
  (cond
    ((eqv? lst nil) nil)
    (#t (let(
              (sub-duplicates (without-duplicates (cdr lst)))
            )
            (if (is-exit sub-duplicates (car lst))
              sub-duplicates
              (cons (car lst) sub-duplicates)
            )
        )
    )
  )
)
