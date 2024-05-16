(define (shrink k t)
  (lambda (s)
    (if (null? s) t
      ( (if (= (car s) k) (shrink (+ k 1) t) (shrink k (cons (car s) t))) 
        (cdr s)) )))

(define-macro (wait expr) `(lambda () ,expr))
(define (double wait-list)
  (if (null? wait-list) nil 
      (cons (* 2 (car wait-list)) (wait (double ((cdr wait-list)))))))

(define twos (cons 2 (wait (double twos))))

(define (promote f s)
  (append (filter f s) (filter (lambda (x) (not (f x))) s)))

(define (cons-me first) (lambda (rest) (cons first rest)))

(define (part n m)
  (cond ((= m n) (list (list n))) 
        ((> m n) nil) 
        (else (append 
                (map (cons-me m) (part (- n m) (+ m 2))) 
                (part n (+ m 1))))))

(define (pairs s) (if (null? s) nil (cons (list (car s) (car (cdr s))) (pairs (cdr (cdr s))))))

(define (group n s) 
  (define (first n s f) 
    (cond ((null? s) nil) 
          ((= n 0) (cons nil (f s))) 
          ((null? (cdr s)) (list (list (car s)))) 
          (else (let ((t (first (- n 1) (cdr s) f))) 
                  (cons (cons (car s) (car t)) (cdr t))))))
  (first n s (lambda (s) (group n s))) )

(define (repeated-call operator operands)
  (if (null? operands) 
    operator
    (repeated-call (list operator (car operands)) (cdr operands))))

(define (curry num-args) 
  (lambda (f) (curry-helper num-args (lambda (s) (apply f s)))))

(define (curry-helper num-args g) 
  (if (= num-args 0) 
    (g nil) 
    (lambda (x) (curry-helper (- num-args 1) (lambda (y) (g (cons x y)))))))

(define (promote f s) (append (filter f s) (filter (lambda (x) (not (f x))) s)))

(define (curry f) (lambda (x) (lambda (y) (f x y))))
(define (curry-call f) (lambda (x g) (lambda (y) (f (x (g y)) y))))

(define bigger-first ((curry-call promote) (curry <) car))

(define (prefix s k) (if (zero? k) nil (cons (car s) (prefix ((cdr s)) (- k 1)))))
(define (add s t) (cons (+ (car s) (car t)) (wait (add ((cdr s)) ((cdr t))))))

(define fib (cons 0 (wait (cons 1 (wait (add fib ((cdr fib)) ) )))))
