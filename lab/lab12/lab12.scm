(define (tail-replicate x n)
  (define-macro (h x) (list '+ x 2))
  (h (+ 2 3))
)

(define-macro (def func args body)
  'YOUR-CODE-HERE)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let (_________________________)
        (* y y y))))
