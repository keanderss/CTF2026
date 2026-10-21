import {
  useEffect,
  useState,
} from "react";

interface CustomCursorProps {
    src: string;
    xOffset: number;
    yOffset: number;
}

const CustomCursor = ({src, xOffset, yOffset}: CustomCursorProps) => {
    const [cords, setCords] = useState({'x': 0, 'y': 0});

    const onMouseMoveEvent = (e: MouseEvent) => {
        const cords = { 'x': e.clientX, 'y': e.clientY };
        setCords(cords);
    }

    useEffect(() => {
        document.addEventListener("mousemove", onMouseMoveEvent);

        return () => {
        document.removeEventListener("mousemove", onMouseMoveEvent);
        };
    }, []);

    return (
        <img
            className="fixed pointer-events-none z-999999"
            style={{
                transform: `translate(${cords.x + xOffset}px, ${cords.y + yOffset}px)`
            }}
            src={src}
            alt=""
        />
    )
} 

export default CustomCursor;