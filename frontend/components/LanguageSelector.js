export default function LanguageSelector({ currentLanguage, onLanguageChange }) {
  return (
    <div className="mb-4">
      <select
        value={currentLanguage}
        onChange={(e) => onLanguageChange(e.target.value)}
        className="w-full p-3 border rounded-lg"
      >
        <option value="en">English</option>
        <option value="ml">Malayalam</option>
      </select>
    </div>
  );
}
