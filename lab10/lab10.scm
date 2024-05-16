
(define (promote f s) (append (filter f s) (filter (lambda (x) (not (f x))) s)))

(define (curry f) (lambda (x) (lambda (y) (f x y))))
(define (curry-call f) (lambda (x g) (lambda (y) (f (x (g y)) y))))

(define bigger-first ((curry-call promote) (curry <) car))
